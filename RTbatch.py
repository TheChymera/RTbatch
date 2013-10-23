#!/usr/bin/env python
__author__ = 'Horea Christian'
from os import path, listdir, walk, remove, makedirs
from string import Template
from chr_helpers import save_gen, get_config_file
import subprocess

def main(do_template=True, do_fullsize=True, do_minis=True, input_file='DSC_a8273.NEF', template_name='octopress'): #tweak do_template and do_export here to controll what output you get
    localpath = path.dirname(path.realpath(__file__)) + '/'
    config = get_config_file(localpath)

    #IMPORT VARIABLES
    scripts_dir = config.get('Directories', 'scripts_dir')
    input_dir = config.get('Directories', 'input_dir')
    output_dir = config.get('Directories', 'output_dir')
    profile_dir = config.get('Directories', 'profile_dir')
    template_dir = config.get('Directories', 'template_dir')
    RT_profiles_dir = config.get('Directories', 'RT_profiles_dir')
    minis_dir = config.get('Directories', 'minis_dir')
    mini_name = config.get('Directories', 'mini_name')
    pictures_link_path = config.get('Directories', 'pictures_link_path')
    input_file = config.get('Parameters', 'input_file')
    template_name = config.get('Parameters', 'template_name')
    if 'octopress' in template_name:
	style = config.get('Parameters', 'style')
    image_width_in_template = config.getint('Parameters', 'image_width_in_template')
    iptc_profile = config.get('Parameters', 'iptc_profile')
    #END IMPORT VARIABLES
    
    if style == 'NONE':
	style = ''
    local_profile_dir = localpath + profile_dir
    profile_list = listdir(RT_profiles_dir)
    profile_list.sort()
    
    if do_template:
	template_file = localpath + template_dir + template_name + '.txt'
	the_template = Template(open(template_file, 'r').read())
	output_template_file = output_dir + path.splitext(input_file)[0] + '-temp'
	outfile = save_gen(output_template_file, extension='.txt')
	
    if do_minis:
	mini_profile_file = local_profile_dir + mini_name
	mini_temp_profile_location = localpath + profile_dir + 'tmp_' + mini_name
	mini_temp_profile_file = save_gen(mini_temp_profile_location)
	mini_profile = Template(open(mini_profile_file, 'r').read())
	mini_temp_profile_file.write(mini_profile.substitute(WIDTH=image_width_in_template))
	mini_temp_profile_file.close()
		
    for profile in profile_list:
	source = localpath+input_dir+input_file
	out_name = path.splitext(input_file)[0]+'-'+profile+'.jpg'
	out_name_minis = path.splitext(input_file)[0]+'-'+profile+'.jpg'
	if do_fullsize:
	    fullsize_destination = localpath+output_dir + out_name.replace(" ", "_")
	    subprocess.call(['rawtherapee', '-o', fullsize_destination, '-p', RT_profiles_dir+profile, '-p', local_profile_dir+input_file+'.pp3', '-p', local_profile_dir+iptc_profile, '-j[100]', '-Y', '-c', source])  # the only ones with their particular identifier
	if do_minis:
	    minis_folder = localpath + output_dir + minis_dir
	    if not path.isdir(minis_folder):
		makedirs(minis_folder)
	    minis_destination = localpath + output_dir + minis_dir + out_name_minis.replace(" ", "_")
	    subprocess.call(['rawtherapee', '-o', minis_destination, '-p', RT_profiles_dir+profile, '-p', local_profile_dir+input_file+'.pp3', '-p', local_profile_dir+iptc_profile, '-p', mini_temp_profile_location, '-j[100]', '-Y', '-c', source])  # the only ones with their particular identifier
	if do_template:
	    full_size_link = pictures_link_path+out_name.replace(" ", "_")
	    mini_path = '/images/photos/minis/'+out_name_minis.replace(" ", "_")
	    outfile.write(the_template.substitute(STYLE=style, PATH=mini_path, WIDTH = image_width_in_template, HEIGHT=0, CAPTION=path.splitext(profile)[0], LINK=full_size_link))
    if do_minis:
	remove(mini_temp_profile_location)
if __name__ == '__main__':
	main()
