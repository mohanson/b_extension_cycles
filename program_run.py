import contextlib
import os
import os.path
import subprocess

@contextlib.contextmanager
def chdir(wd):
    cwd = os.getcwd()
    os.chdir(wd)
    try:
        yield wd
    finally:
        os.chdir(cwd)

with chdir('bin'):
    subprocess.call('cargo build --release', shell=True)

# /src/pin-3.18-98332-gaebd7b1e6-gcc-linux/source/tools/ManualExamples
# https://software.intel.com/content/www/us/en/develop/articles/pin-a-binary-instrumentation-tool-downloads.html
# https://stackoverflow.com/questions/19093796/how-can-i-use-the-intel-pin-tool-to-count-the-instruction-executed-on-linux

for e in os.listdir('program'):
    if '.' not in e:
        print(e, end=' ')
        abs_path = os.path.abspath(os.path.join('program', e))

        with chdir('/src/pin-3.18-98332-gaebd7b1e6-gcc-linux/source/tools/ManualExamples'):
            r = subprocess.getoutput(f'../../../pin -t obj-intel64/inscount0.so -- /src/b_extension_cycles/bin/target/release/bin {abs_path}')
            r = subprocess.getoutput('cat inscount.out')
            print(r.split()[1])

        # r = subprocess.getoutput(f'valgrind --tool=callgrind bin/target/release/bin program/{e}')

subprocess.call('rm -rf callgrind*', shell=True)
