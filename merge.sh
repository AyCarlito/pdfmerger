#!/usr/bin/env sh


echo "Installing requirements"

pip install -r requirements.txt

echo "Merging PDFs"

python -u pdfmerger
