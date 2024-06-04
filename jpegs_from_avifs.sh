for i in *.avif;
	do name=`echo $i | cut -d '.' -f1`;
	echo $name;
	~/sft/opt/libheif/examples/heif-convert "$i" "${name}.jpeg";
	rm "${name}.avif"
done
