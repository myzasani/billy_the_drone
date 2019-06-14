import tello

# Billy
billy = tello.Tello()

# Each leg of the box will be 100 cm. Tello uses cm units by default.
box_leg_distance = 30

# Yaw 90 degrees
yaw_angle = 90

# Yaw clockwise (right)
yaw_direction = "cw"

# Put Tello into command mode
billy.send("command", 3)

# Send the takeoff command
billy.send("takeoff", 5)

# Fly forward
billy.send("forward " + str(box_leg_distance), 4)

# Turn clock-wise
billy.send("cw " + str(yaw_angle), 3)

# Flip back
billy.send("flip b ", 4)


#billy.send("curve 25 -25 0 25 -75 0 20", 20)


# # Fly forward
# send("forward " + str(box_leg_distance), 4)
#
# # Yaw right
# send("cw " + str(yaw_angle), 3)
#
# # Fly forward
# send("forward " + str(box_leg_distance), 4)
#
# # Yaw right
# send("cw " + str(yaw_angle), 3)
#
# # Fly forward
# send("forward " + str(box_leg_distance), 4)
#
# # Yaw right
# send("cw " + str(yaw_angle), 3)

# Land
billy.send("land", 3)

# Print message
print("Mission completed successfully!")

# Close the socket
billy.sock.close()
