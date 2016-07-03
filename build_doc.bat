sphinx-build -b htmlhelp doc doctmp
"C:\Program Files\HTML Help Workshop\hhc.exe" doctmp\plotpy.hhp
"C:\Program Files (x86)\HTML Help Workshop\hhc.exe" doctmp\plotpy.hhp
copy doctmp\plotpy.chm .
7z a plotpy.chm.zip plotpy.chm
del doctmp\plotpy.chm
del doc.zip
del doctmp\plotpy.hh*
sphinx-build -b html doc doctmp
cd doctmp
7z a -r ..\doc.zip *.*
cd ..
rmdir /S /Q doctmp
del plotpy.chm.zip