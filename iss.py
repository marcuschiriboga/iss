#!/usr/bin/env python

__author__ = 'marcus w/ peter mayor'
import requests
import turtle
import time


def print_team():
    """prints the humans in space"""
    r = requests.get('http://api.open-notify.org/astros.json')
    r = r.json()
    crew = r["people"]
    print("the people in space are")
    for name in crew:
        print(name["name"])
    print()


def render_with_turtle(x, y, when):
    """handles drawing and writing in turtle"""
    turtle.setup(width=720, height=360, startx=0, starty=0)
    turtle.setworldcoordinates(-180, -90, 180, 90)
    screen = turtle.Screen()
    screen.bgpic("map.gif")
    screen.register_shape("iss.gif")
    iss = turtle.Turtle()
    iss.goto(-86.1581, 39.7684)
    iss.dot(10, "yellow")
    iss.color("white")
    iss.write(when, font=("Arial", 16))
    iss.color("black")
    iss.shape("iss.gif")
    iss.goto(x, y)
    turtle.done()
    pass


def get_iss_location():
    """handle requests to space and return coordinates to iss"""
    r = requests.get('http://api.open-notify.org/iss-now.json')
    r_json = r.json()
    lon = float(r_json["iss_position"]["longitude"])
    lat = float(r_json["iss_position"]["latitude"])
    return lon, lat


def get_time_over_indy():
    """when will iss next pass over indy"""
    r = requests.get(
        "http://api.open-notify.org/iss-pass.json?lat=39.7684&lon=-86.1581&n=1"
    )
    r_json = r.json()
    print("the next time it'll be over indy is:")
    print(time.ctime(r_json["response"][0]["risetime"]))
    return time.ctime(r_json["response"][0]["risetime"])


def main():
    """call all the functions"""
    print_team()
    time_over = get_time_over_indy()
    lon, lat = get_iss_location()
    render_with_turtle(lon, lat, time_over)
    pass


if __name__ == '__main__':
    main()
