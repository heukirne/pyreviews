cd reviews
find -name "* *" -type d | rename 's/ /_/g'
find . -name "*.txt" -type f -delete
for file in $(pcregrep -MlrI "<thumbsUp value=\"0\"/>(\n).*<thumbsDown value=\"0\"/>")
do 
	rm $file
done