# -interaction nonstopmode makes error not halt in shell
# -file-line-error shows the location in the tex file of the error
all :
	xelatex -interaction nonstopmode -file-line-error swaps.tex
