

import os
import pathlib
import pywinauto
import time

working_folder='C:\\Users\\EI Administrator\\Desktop\\NSLS2_Data_Processing\\20190321_NSLS2_SRX_Data\\beamline_data\\23581_to_23708_xrd_tiffs\\'
os.chdir(working_folder)

object_list_allfilesdirectories = pathlib.Path('.')
object_recursiveglob = object_list_allfilesdirectories.glob('*.tif')
object_list_filenames = list(object_recursiveglob)


for i in range(0,len(object_list_filenames)):
    filenamebase=object_list_filenames[i].name[0:-4]
    path_and_filename = str(object_list_filenames[i].parents[0].joinpath(object_list_filenames[i].parts[-1][0:-4]+'_datasqueeze.txt'))
    #shutil.copyfile("./data_squeeze_template_file.txt",path_and_filename)
    print(path_and_filename)

    with open(path_and_filename, "w") as f:
        f.write('>READFILE 0  \"' + working_folder + path_and_filename[0:-16] + '.tif" "Tiff"  false 0 1 -1\n') #
        f.write('>READFILE 1  \"C:\\Users\\EI Administrator\\Desktop\\NSLS2_Data_Processing\\20190321_NSLS2_SRX_Data\\beamline_data\\23580_xrd_darkfield\\MED_scan2D_23580.tif" "Tiff"  false 0 -1 -1\n') #
        f.write('>RECALCIMAGE\n')
        f.write('>RETRIEVEINSTRUMENTPARAMETERS "C:\\Users\\EI Administrator\\Desktop\\NSLS2_Data_Processing\\20190321_NSLS2_SRX_Data\\beamline_data\WAXS_detector_param.txt"\n')
        f.write('>RECALCIMAGE\n')
        f.write('>DEZING\n')
        f.write('>RECALCIMAGE\n')
        f.write('>PLOT false false false Q 1.270 6.135 5.000E-4 CHI -50.000 50.000 1.323  0\n')
        f.write('>EXPORTPLOT \"' + working_folder + path_and_filename[0:-4] + '_1D_data.txt" ASCII2COLUMN CSV\n')

    time.sleep(1)
    window_handle=pywinauto.findwindows.find_windows(title='False Color Image')
    app=pywinauto.application.Application().connect(handle=window_handle[0])
    time.sleep(1)
    app.top_window().type_keys('^B')
    time.sleep(1)
    topwin=app.top_window()
    app.top_window().set_focus()
    time.sleep(1)
    app.top_window().type_keys(object_list_filenames[i].parts[-1][0:-4]+'_datasqueeze.txt')
    app.top_window().set_focus()
    time.sleep(1)
    pywinauto.keyboard.send_keys('{ENTER}')
    time.sleep(20)
    #window_coordinates=topwin.rectangle()
