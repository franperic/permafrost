<div>
<img src="./00_input/image001.jpg" alt="header" width="750"/>
</div>
<br>
<br>

# Unsupervised Movement Detection

## Overview
This repo is a summary of the Permafrost Hackathon, which took place at the ETH Zurich end of November 2019.
For more background information check the following [blogpost](https://www.statworx.com/ch/blog).

The presented code and approach is the result of Team Aroma.
Visit the Hackathon [repo](https://github.com/ETHZ-TEC/permafrostanalytics) for other contributions.

## Data
Visit the above mentioned hackathon repo to download the relevant data source.
For reproducability only the data source `timelapse_images_fast.zip` is necessary.

### Folder Structure
Make sure your folder structure looks like this:

```
.
├── 00_input
│   └── image001.jpg
├── 01_data
│   └── timelapse_images_fast
│       ├── 2017-01-01
│           ├── 20170101_070009.JPG
│           ├── 20170101_070409.JPG
│           └── ...
│       ├── 2017-01-02
│       └── ...
├── 02_code
│   ├── helperfunctions.py
│   └── movement_detection.py
├── LICENSE
├── README.md
├── requirements.txt
└── setup.sh
```

## Contact
If there are any questions, don't hesitate to shoot me an [email](fran.peric@statworx.com).