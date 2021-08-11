echo "Lauching VMPW"
cd C:\Users\tonup\work\vj_dev_env
conda activate vjdev
code .\
$Env:WASMTIME_BACKTRACE_DETAILS = 1
python .\QtLive\embedded_IPython.py
# .\vmpw\things\systems\wasmerLoader.py