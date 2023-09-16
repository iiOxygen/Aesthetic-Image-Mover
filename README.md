This is a basic Python script, coded by AI, that sorts PNG images based on their aesthetic score. The aesthetic score is extracted from the metadata of images generated using the Stable Diffusion WebUI Aesthetic Image Scorer. 
(https://github.com/tsngo/stable-diffusion-webui-aesthetic-image-scorer)

**Overview**

The script processes a folder containing PNG images and sorts them into sub-folders based on their aesthetic score. Images with an aesthetic score of 7.0 or higher are placed in the "aesthetic" folder, while those with a lower score are placed in the "not_aesthetic" folder. Additionally, images are sorted into decimal folders based on their exact aesthetic score.

**Usage**

Clone the repo:
```
git clone https://github.com/iiOxygen/SD-WebUI-Aesthetic-Image-Mover.git
```

Install the required dependencies:

```
pip install Pillow
```

Modify the config.ini file with the following content:

```
[Paths]
root_folder = insert\\folder\\path\\here
output_folder = insert\\output\\folder\\path\\here
```
Replace ``insert\\folder\\path\\here``
 with the paths to the folder containing the PNG images you want to process and the output folder, respectively.

Run the script:

```
python Mover.py
```

For obvious reasons, I recommend using https://github.com/dvruette/sd-webui-fabric along with the main extension.
