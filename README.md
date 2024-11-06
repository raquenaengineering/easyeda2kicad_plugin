# LCSC Importer for KiCad

A KiCad plugin that allows you to easily import parts (symbols, footprints, and 3D models) from LCSC directly into KiCad, using the easyeda2kicad command line tool.

### Key Features
- **Seamless Import**: Quickly import LCSC parts by entering their part number.
- **Direct Access**: Integrated into the toolbar for easy access within the PCB editor.
  
![Toolbar Screenshot](https://github.com/user-attachments/assets/d925aedc-483a-429f-ae3e-cf4fea454317)

### How It Works
1. **Enter LCSC Part Number**: Type in the LCSC part number to import its symbol, footprint, and 3D model directly into KiCad.

![Import Menu Screenshot](https://github.com/user-attachments/assets/8438877e-8ba5-46f7-bc8d-0552915c4243)

2. **Auto-Save**: Imported parts are stored in `/KiCad/easyeda2kicad`, ready for use.

---

## Installation

1. **Clone the Repository**  
   Clone this repository to your downloads folder.

2. **Move Files to KiCad Plugin Folder**  
   Move all contents to your KiCad plugins directory:  
   `KiCad/(version)/scripting/plugins`

4. **Organize the Files**  
   Ensure `LCSC Importer.py` is not inside any subfolder.

5. **Install dependencies**  
   When you first launch KiCad, you may be missing one or more dependencies to run the plugin inside KiCad. Install these using pip.
   On Windows you may have to install this through the _KiCad Command Promt_ found in programs/KiCadX/.

6. **Run the plugin**  
   Once all dependencies are installed, run the plugin from the top menu bar in the PCB editor, and import your first component!
   This will generate the required libraries, KiCad needs to import your parts.

8. **Add libraries in KiCad**  
   Lastly, we just need to tell KiCad where to find the parts you import!

  - In KiCad, Go to Preferences > Configure Paths, and add the environment variables `EASYEDA2KICAD` :
    - Windows : `C:/Users/your_username/Documents/Kicad/easyeda2kicad/`,
    - Linux : `/home/your_username/Documents/Kicad/easyeda2kicad/`
  - Go to Preferences > Manage Symbol Libraries, and Add the global library `easyeda2kicad` : `${EASYEDA2KICAD}/easyeda2kicad.kicad_sym`
  - Go to Preferences > Manage Footprint Libraries, and Add the global library `easyeda2kicad` : `${EASYEDA2KICAD}/easyeda2kicad.pretty`

---

Enjoy simplified part importing from LCSC directly into your KiCad designs!
