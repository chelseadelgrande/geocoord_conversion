import mgrs
import pandas as pd
import xlsxwriter

#read excel file
df = pd.read_excel("Full_path_here.xlsx",
            sheet_name = 'sht_name')
df.head()

#pull column of interest
df2 = df["GPS_Coord"]

#convert mgrs to dd
m = mgrs.MGRS()

#for record in column of interest, convert to latlong
mrgs = []
dd= []
for x in df2:
    try:
        a = bytes(x, 'utf-8')
        latlon = m.toLatLon(a)
        #print(x, latlon)
       
        mrgs.append(x)
        dd.append(latlon)
    except TypeError:
        print ('Error:', TypeError)
        continue
#print(mrgs, dd)
coords_total = dict(zip(mrgs, dd))
print (coords_total)

#for export
workbook = xlsxwriter.Workbook("new_path_here")
worksheet = workbook.add_worksheet()

row = 0
col = 0
for key in coords_total.keys():
    row+=1
    worksheet.write(row, col, key)
    for item in coords_total[key]:
        worksheet.write(row, col+1, item)
        row+=1
workbook.close()
#print(mrgs, dd)
        #df2.to_excel("Out_Path_Here.xlsx", columns = ['mrgs', 'dd']) 
    #if error in log, continue iterating
    #except TypeError:
        #print ('Error:', TypeError)
        #continue
#coords_total = dict(zip(mrgs, dd))
#print (coords_total)

    
