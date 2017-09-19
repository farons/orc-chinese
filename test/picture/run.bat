rem 执行改批处理前先要目录下创建font_properties文件 

echo Run Tesseract for Training.. 
tesseract.exe mjorcen.normal.exp0.tif mjorcen.normal.exp0 nobatch box.train 
 
echo Compute the Character Set.. 
unicharset_extractor.exe mjorcen.normal.exp0.box 
shapeclustering.exe -F font_properties.txt -U unicharset mjorcen.normal.exp0.tr
mftraining -F font_properties.txt -U unicharset -O unicharset mjorcen.normal.exp0.tr 


echo Clustering.. 
cntraining.exe mjorcen.normal.exp0.tr 

echo Rename Files.. 
rename unicharset normal.unicharset 
rename normproto normal.normproto 
rename inttemp normal.inttemp 
rename pffmtable normal.pffmtable 
rename shapetable normal.shapetable  

echo Create Tessdata.. 
combine_tessdata.exe normal. 

echo. & pause