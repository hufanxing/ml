
file=$1
out_file='unregistered.txt'
rm -f $out_file
list=`cat $file`

for domain in $list
do
    # domain='sfdafdaba9dabi.com'
    str=`whois $domain | sed -n '8p' | cut -c1-12` 
    if [ "$str" = "No match for" ]; then
	echo $domain >> $out_file
	echo "find one $domain"
    else
	echo "$domain is registered"
    fi
done

