# Python에서 xml file 다루기

## xml 파일 읽기

[data.xml 예제]

```xml
<annotation>
    <folder>20190326</folder>
    <filename>0_14_0_10[153x112].JPG</filename>
    <size>
        <width>4608</width>
        <height>3456</height>
        <depth>3</depth>
    </size>
    <segmented>0</segmented>
    <object>
        <name>Drone2</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <occluded>0</occluded>
        <difficult>0</difficult>
        <bndbox>
            <xmin>2216</xmin>
            <ymin>787</ymin>
            <xmax>2433</xmax>
            <ymax>950</ymax>
        </bndbox>
    </object>
</annotation>
```

```python
import xml.etree.ElementTree as ET

file_name = 'data.xml'

doc = ET.parse(file_name)

root = doc.getroot()

objs = root.findall('object')   # Find object in the xml

for obj in objs:
  target = {}
  obj_name = obj.findtext('name')
  obj_bbox = obj.findall('bndbox')
  for bbox in obj_bbox:
    xmin = int(bbox.findtext('xmin'))
    ymin = int(bbox.findtext('ymin'))
    xmax = int(bbox.findtext('xmax'))
    ymax = int(bbox.findtext('ymax'))
  print('Object: {}, bbox:({}, {}, {}, {})'.format(obj_name,
          xmin, ymin, xmax, ymax))

```

## CSV 파일 쓰기

```python
import csv
f = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow([1, "Kevin", False])
wr.writerow([2, "Halsey", True])
f.close()
```

##### [[Python 돌아가기]](README.md) | [[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
