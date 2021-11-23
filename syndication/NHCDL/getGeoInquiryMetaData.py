from arcgis.gis import GIS
gis = GIS('https://www.arcgis.com', 'tbakerk12', 'naish101')
import csv
print('')
print("CR_Title,CR_Author_Name,CR_Provider,CR_Create_Date,CR_Provider_St,CR_Language,CR_URL,CR_Media_Formats,CR_Material_Type,CR_Subject,CR_Keywords,CR_COU_TITLE,CR_COU_URL,CR_Abstract,CR_Educational_Use,CR_Primary_User,CR_Sublevel,CR_WORKFLOW_STATE")

with open('data/geoinquiry_ids.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        row = str(row).replace("[","").replace("]","").replace("'","")
        results = gis.content.search("id:"+row, max_items=2, outside_org=True)
        for record in results:
            snippet=record.snippet.replace(",","")
            tags=str(record.tags).replace("'","").replace(", ","|").replace("[","").replace("]","")
            if tags is '':
                tags = 'geoinquiry'
            CNstart = record.title.find('collection for') + 14
            CN=record.title[CNstart:len(record.title)]
            print(record.title.replace(",",""), ',Esri,Esri,2021/11/23,', CN, ',en,https://arcgis.com/home/item.html?id=',record.id,',Downloadable docs|Interactive,Lesson|Activity/Lab|Interactive,CR_Subject,', tags, ',Creative Commons Attribution Non-Commercial Share Alike,https://creativecommons.org/licenses/by-nc-sa/4.0/,', snippet, ',Curriculum/Instruction,Teachers|Students,Middle School|High School', sep="" )

