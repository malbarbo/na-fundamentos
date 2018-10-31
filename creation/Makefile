all:
	rm -rf ../target/creation/
	mkdir -p ../target/creation/
	PYTHONDONTWRITEBYTECODE=1 ./color-map.py
	PYTHONDONTWRITEBYTECODE=1 ./gen.py \
		circle.py \
		ellipse.py \
		triangle.py \
		square.py \
		rectangle.py \
		text.py \
		pixmap.py \
		beside.py \
		above.py \
		overlay.py \
		place.py
	for f in ../target/creation/*.svg; do rsvg-convert $$f -x 0.8 -y 0.8 -f pdf -o ../target/creation/$$(basename $$f .svg).pdf; done
