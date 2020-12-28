# TCIA dataset extraction


The solution is based on these [repository](https://github.com/hilfikerp/TCIA-Python3-Downloader.git) and [api](https://wiki.cancerimagingarchive.net/display/Public/TCIA+Programmatic+Interface+%28REST+API%29+Usage+Guide).


## usage:
```
cd /opt/data/user/dobreknii/data/DDSM
mkdir -p /opt/data/user/dobreknii/data/DDSM/TCIA_DATA
python3 TCIA_READER/tcia_from_file.py -f ../CBIS-DDSM-All-doiJNLP-zzWs5zfZ.tcia -d ../TCIA_DATA/ > ../tcia.log 2>&1 &
```
