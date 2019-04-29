# Demos seemed to be interesting

- [Pedestrian Detection in Aerial Images using RetinaNet](https://www.youtube.com/watch?v=KXBknhy_kjw)

  > [GitHub](https://github.com/priya-dwivedi/aerial_pedestrian_detection)

  > [Standford Aerial Dataset(69G)](http://vatic2.stanford.edu/stanford_campus_dataset.zip) used in the project.

  > [Keras-RetinaNet Implementation](https://github.com/fizyr/keras-retinanet) used as well.

## Brief Cheat from the blog above

### Training Custom data set

For training on a [custom dataset], a CSV file can be used as a way to pass the data. See below for more details on the format of these CSV files.

To train using your CSV, run:

```bash
keras_retinanet/bin/train.py --weights snapshots/resnet50_coco_best_v2.1.0.h5 csv train_annotations.csv labels.csv --val-annotations val_annotations.csv
```

Here

> weights: Path to the weights for initializing training
>
> csv indicates retinanet is trained on a custom data set
>
> rain_annotations.csv is path to training annotations
>
> labels.csv are the labels in the format class_name, class_id with 0 reserved for background class
> val_annotations is path to validation annotations

### Annotation Format

The CSV file with annotations should contain one annotation per line. Images with multiple bounding boxes should use one row per bounding box. Note that indexing for pixel values starts at 0. The expected format of each line is:

```bash
path/to/image.jpg,x1,y1,x2,y2,class_name
```

> May use the Trainig Data (by Priyanka Dwinvedi)
>
> > use [Priyanka Dwinvedi's dataset](https://drive.google.com/drive/u/0/folders/1bLt6KK_9zKogJdvW-lKh9BnBKgFfvPp9)

### Label Format

The class name to ID mapping file should contain one mapping per line. Each line should use the following format:

```bash
class_name,id
```

For the Stanford Drone Data Set, the training annotations are in train_annotations.csv, validation annotations are in val_annoations.csv and labels are in labels.csv
