from collections import OrderedDict

obj_detected = {'bottle': [110, 30], 'glass': [60, 35], 'book': [310, 23], 'phone': [90, 33], 'dice': [155, 38], 'mouse':
[200, 45], 'keyboard': [298, 65], 'fan': [300, 36]}

sort_obj_detected = sorted(obj_detected.items(), key = lambda x : x[1])

new_obj_detected = OrderedDict(sort_obj_detected)

for k , v in new_obj_detected.items():
    print(k)


