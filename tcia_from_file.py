import tciaclient as tc
import os, urllib.request, urllib.error, urllib.parse, urllib.request, urllib.parse, urllib.error, sys
import argparse
from tqdm import tqdm


#  get parameters from command line
parser = argparse.ArgumentParser()

parser.add_argument(
    "-f", '--tcia-file-path',
    required=True,
    help="""Path to the TCIA file with DICOM ListOfSeriesToDownload:
    ...
    ListOfSeriesToDownload=
    1.3.6.1.4.1.9590.100.1.2.294445047912407030012248838470114617726
    1.3.6.1.4.1.9590.100.1.2.188613955710170417803011787532523988680
    1.3.6.1.4.1.9590.100.1.2.399466258212646932018425683324156637601
    1.3.6.1.4.1.9590.100.1.2.419081637812053404913157930753972718515
    1.3.6.1.4.1.9590.100.1.2.284547955212024760928760792420660349691
    """)

parser.add_argument(
    '-d', '--dst-path',
    default='.',
    help="""Output path to save DICOM files.
         If parameters is not set then converted file or dir with converted
         files will be created near to TCIA file""")

parser.add_argument(
    '--postfix',
    default=False, action='store_true',
    help='Add postfix to filenames _{i}, where `i` is slice order in DICOM'
)

args = parser.parse_args()

####################################  Function to print server response #######
def printServerResponse(response):
    if response.getcode() == 200:
        print("Server Returned:\n")
        print(response.read())
        print("\n")
    else:
        print("Error: " + str(response.getcode()))


tcia_client = tc.TCIAClient()
studyInstanceUIDStrings = tc.read_tcia_file(args.tcia_file_path)

for uid in tqdm(studyInstanceUIDStrings):
    filename = uid + '.zip'
    try:
        response = tcia_client.get_image(
            seriesInstanceUid=uid, downloadPath=args.dst_path, 
            zipFileName=filename
        )
    except:
        print("\nError executing program.  Please verify input.\n")
