#!/bin/sh
new_dir=new
if [ -d $new_dir ]; then
    rm $new_dir -rf
fi
mkdir $new_dir

echo "start"
for file in *; do
    if [ -d "$file" ]; then
    no_space_file=`echo "$file" | sed 's/ /./g'`
    mv "$file" "$no_space_file"
        if [ "$no_space_file" != "$new_dir" ]; then
            echo "deal $no_space_file"
            cd $no_space_file
            for subfile in *; do
                no_space_subfile=`echo "$subfile" | sed 's/ /./g'`
                echo "mv $no_space_subfile"
                if [ -f $no_space_subfile ]; then
                    new_subfile="$no_space_file:$no_space_subfile"
                    cp "$subfile" "../$new_dir/$new_subfile"
                fi
            done
            cd ../
        fi
    fi
done
echo "end"
