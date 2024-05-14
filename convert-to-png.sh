for f in out/*; do
  inkscape -w 128 -h 128 "$f" -o "${f%.*}.png"
done

mkdir out-png

mv out/*png out-png

