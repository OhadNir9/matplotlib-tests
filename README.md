findings:
1. more 'objects' (like the collections objects that scatter calls create) increases the latency significantly.
2. draw_idle is the same as draw, but only draws when the control is back in the hands of the GUI event loop. This is significantly faster then 'draw'ing everytime in case of long functions. In general, it is good to call the 'draw'/'update' functions the minimum required times (they are very expensive). For example, only draw after 10/30 points.
3. Altough 'generate_unefficient' execution time grows monotonically, it starts from relatively low numbers.
This means that if I'll buffer the consequtive calls, it'll be gooood enough
