import subprocess
import sys
def test_script_output(capfd):
    
    #run the script file under a new process using the same python interpretor
    subprocess.run([sys.executable,'../script.py'])
    
    #capture the process output
    captured = capfd.readouterr()
    
    #assert that the output is correct
    assert captured.out == "Hello World!\r\n"
