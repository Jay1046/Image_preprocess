import click
import sys
from preprocess.roi_json import ROI1
from preprocess.roi_jpg import ROI2
from preprocess.roi_mask import ROI3



@click.command()
@click.option('-m', '--roi-operation', type=click.STRING, default='', help="ROI type")
def operate_roi(roi_operation):
    try:
        if roi_operation == "json":
            roi = ROI1()
            roi.save()
        if roi_operation == "jpg":
            roi = ROI2()
            roi.save()
        if roi_operation == "mask":
            roi = ROI3()
            roi.save()
    except Exception as e:
        print(e)
        sys.exit(1)
    sys.exit(0)



if __name__ == '__main__':
    print("start ROI operation")
    operate_roi()
    print("end ROI operation")


