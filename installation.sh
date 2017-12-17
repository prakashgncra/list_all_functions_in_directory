# define various paths
bashfun='.github_extras/bash_functions.sh'
basedir='.github_extras/list_all_functions/'

# Make directory move files is necessary
mkdir -p ~/$basedir
cp list_functions.py ~/$basedir'list_functions.py'

# Write the bash function, aliases for system wide access
echo "" >> ~/$bashfun
echo "#--------------- list_all_functions aliases ----------------" >> ~/$bashfun
echo "" >> ~/$bashfun
echo 'function list_all_functions()' >> ~/$bashfun
echo '{' >> ~/$bashfun
echo 'python '~/$basedir'list_functions.py $(echo $PWD)' >> ~/$bashfun
echo '}' >> ~/$bashfun
echo '' >> ~/$bashfun
echo "" >> ~/$bashfun

# Check if .github_extras/bash_functions.sh is source in bashrc
SOURCE_STRING='source ~/'$bashfun
if [[ ! -z $(grep "$SOURCE_STRING" ~/.bashrc) ]]
then 
source ~/$bashfun
echo "File "$SOURCE_STRING" is sourced ..."
else
echo $SOURCE_STRING >> ~/.bashrc 
source ~/.bashrc 
echo "File .bashrc and "$SOURCE_STRING" is sourced ..."
fi

