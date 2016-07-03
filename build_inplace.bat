rmdir /S /Q build
del plotpy\*.pyd
python setup.py --no-user-cfg build_ext -c msvc --inplace --sse2