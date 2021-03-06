cd reviews
find -name "* *" -type d | rename 's/ /_/g'
find . -name "*.txt" -type f -delete
for dir in $(ls)
do
	echo "removing from $dir"
	for sub in $(ls $dir)
	do
		echo "removing from $dir/$sub"
		for file in $(pcregrep -MlrI "<thumbsUp value=\"0\"/>(\n).*<thumbsDown value=\"0\"/>" $dir/$sub)
		do 
			rm $file
		done
	done
done