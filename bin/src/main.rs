use ckb_vm::registers::{A0, A7};
use ckb_vm::Register;
use ckb_vm::SupportMachine;
use ckb_vm::Syscalls;

mod convention;
mod cost_model;

pub struct CustomSyscall {}

impl<Mac: SupportMachine> Syscalls<Mac> for CustomSyscall {
    fn initialize(&mut self, _: &mut Mac) -> Result<(), ckb_vm::Error> {
        Ok(())
    }

    fn ecall(&mut self, machine: &mut Mac) -> Result<bool, ckb_vm::Error> {
        let code = &machine.registers()[A7];
        if code.to_i32() != 1111 {
            return Ok(false);
        }
        let result = Mac::REG::zero();
        machine.set_register(A0, result);
        Ok(true)
    }
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args: Vec<String> = std::env::args().collect();
    let code_data = std::fs::read(&args[1])?;
    let code = bytes::Bytes::from(code_data);

    let asm_core =
        ckb_vm::machine::asm::AsmCoreMachine::new(convention::ISA, convention::VERSION, u64::MAX);
    let core =
        ckb_vm::DefaultMachineBuilder::<Box<ckb_vm::machine::asm::AsmCoreMachine>>::new(asm_core)
            .instruction_cycle_func(Box::new(cost_model::instruction_cycles))
            .syscall(Box::new(CustomSyscall {}))
            .build();
    let mut machine = ckb_vm::machine::asm::AsmMachine::new(core, None);
    machine.load_program(&code, &vec!["main".into()]).unwrap();

    let exit = machine.run();
    assert_eq!(exit.unwrap(), 0);

    Ok(())
}
