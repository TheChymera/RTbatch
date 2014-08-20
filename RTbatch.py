__author__ = 'Horea Christian'
from os import path, listdir, walk, remove, makedirs
from string import Template
from chr_helpers import save_gen, get_config_file
import subprocess

def main(input_file, output_dir="", iptc_profile="", do_fullsize=True, do_minis=True, template_name="", mini_width=""): #tweak do_template and do_export here to controll what output you get
	localpath = path.dirname(path.realpath(__file__)) + '/'
	config = get_config_file(localpath)

	#IMPORT VARIABLES
	if not output_dir:
		output_dir = localpath+config.get('Directories', 'output_dir')
	else:
		output_dir = path.expanduser(output_dir)
	batch_profile_dir = config.get('Directories', 'batch_profile_dir')
	template_dir = config.get('Directories', 'template_dir')
	RT_profiles_dir = config.get('Directories', 'RT_profiles_dir')
	minis_dir = config.get('Directories', 'minis_dir')
	mini_name = config.get('Directories', 'mini_name')
	pictures_link_path = config.get('Directories', 'pictures_link_path')
	if 'octopress' in template_name:
		style = config.get('Parameters', 'style')
	if not mini_width:
		mini_width = config.getint('Parameters', 'mini_width')
	#END IMPORT VARIABLES
	
	if style == 'NONE':
		style = ''
	
	if not iptc_profile:
		iptc_profile = batch_profile_dir+iptc_profile
	else:
		iptc_profile = path.abspath(path.expanduser(iptc_profile))
	
	input_file = path.abspath(path.expanduser(input_file))
	batch_profile_dir = localpath + batch_profile_dir
	
	profile_list = []
	for lepath, subdirs, files in walk(RT_profiles_dir):
		for name in files:
			profile_list += [path.join(lepath, name)]
	    
	if bool(template_name):
		template_file = localpath + template_dir + template_name + '.txt'
		the_template = Template(open(template_file, 'r').read())
		output_template_file = output_dir + path.splitext(path.basename(input_file))[0] + '-temp'
		outfile = save_gen(output_template_file, extension='.txt')
	
	if do_minis:
		mini_profile_file = batch_profile_dir + mini_name
		mini_temp_profile_location = batch_profile_dir + 'tmp_' + mini_name
		mini_temp_profile_file = save_gen(mini_temp_profile_location)
		mini_profile = Template(open(mini_profile_file, 'r').read())
		mini_temp_profile_file.write(mini_profile.substitute(WIDTH=mini_width))
		mini_temp_profile_file.close()
		
	for profile in profile_list:
		source = input_file
		out_name = path.splitext(path.basename(input_file))[0]+'-'+path.basename(profile)+'.jpg'
		out_name_minis = path.splitext(path.basename(input_file))[0]+'-'+path.basename(profile)+'.jpg'
		if do_fullsize:
			fullsize_destination = output_dir + out_name.replace(" ", "_")
			subprocess.call(['rawtherapee', '-o', fullsize_destination, '-p', iptc_profile, '-p', profile, '-j[100]', '-Y', '-c', source])  
		if do_minis:
			minis_folder = output_dir + minis_dir
			if not path.isdir(minis_folder):
				makedirs(minis_folder)
			minis_destination = output_dir + minis_dir + out_name_minis.replace(" ", "_")
			subprocess.call(['rawtherapee', '-o', minis_destination, '-p', iptc_profile, '-p', profile, '-p', mini_temp_profile_location, '-j[100]', '-Y', '-c', source])
		if bool(template_name):
			full_size_link = pictures_link_path+out_name.replace(" ", "_")
			mini_path = '/images/photos/minis/'+out_name_minis.replace(" ", "_")
			outfile.write(the_template.substitute(STYLE=style, PATH=mini_path, WIDTH = mini_width, HEIGHT=0, CAPTION=path.splitext(profile)[0], LINK=full_size_link))
	if do_minis:
		remove(mini_temp_profile_location)

if __name__ == '__main__':
	main()
