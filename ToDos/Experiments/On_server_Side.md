# 실험 정리

## YOLOv3 Test:

- Snapshots and Weights:

  - logs/
    - 000/ temp snapshots
    - 001/ tmp snapshots

---

- Main Backup Snapshots w/ Weights

  - logs/backup

    - /20190509 Old backups for insufficient DataSetups (test purpose)
    - /20190510 Similar to 0509 Test. Also default config used.
    - /20190512 Now consolidate Dataset (D201904\*02_05_08_10) used

      -         But still default anchor and input (416,416) used

    - /20190513_HR Input Resolution increased to (32 \* 35, 32 \* 35)
      The purpose of this high resolution is to see
      how higher resolution can effect on small object deteion

                                    Also, New Anchors for our custom dataset are used.
                                    Since input to NWK is squared shape,
                                    I reflected those warped shaped to compute anchors.
                                    The anchors are obtained using k-mean clustering.

The new anchor is stored in:
/model_data/yolo_anchors_translated_HR_0513.txt
Video Test:
aerial_pedestrian_detection/video/DSCN1258_yolov3_new_anchor_HR_0513.MP4
/20190514_HRWarp
Also, used (32*35, 32*35) resolution to train the model.
However, anchor is not corrected to reflect squaring shape
The new anchor is stored in:
/model_data/yolo_anchors_translated_HR_0513_warped.txt

                        Video Test:
                        aerial_pedestrian_detection/video/DSCN1258_yolov3_new_anchor_HR_warp_0514444.MP4
