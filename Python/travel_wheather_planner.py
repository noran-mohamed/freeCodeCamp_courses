distance_mi = 50
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = False

if not distance_mi:
    print("False")

if distance_mi <= 1 and not is_raining:
    print("True")


elif distance_mi > 1 and distance_mi <= 6 and not is_raining and has_bike:
    print("True")

elif distance_mi > 6 and (has_car or has_ride_share_app):
    print("True")
else:
    print("False")
