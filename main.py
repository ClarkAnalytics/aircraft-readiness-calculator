def main():
    total_aircraft = int(input("Enter total aircraft: "))
    operational_aircraft = int(input("Enter operational aircraft: "))
    avionics = int(input("Enter number of aircraft down for avionics: "))
    flight_controls = int(input("Enter number of aircraft down for flight controls: "))
    icing = int(input("Enter number of aircraft down for icing: "))
    total_readiness = readiness_percent(total_aircraft, operational_aircraft)
    total_down = total_aircraft - operational_aircraft
    print(f"Aircraft Readiness Percentage: {total_readiness:.1f}%\n\n"
          f"Down Aircraft Breakdown:\n"
          f"Avionics: {avionics}\n"
          f"Flight Controls: {flight_controls}\n"
          f"Icing: {icing}\n\n"
          f"Total Down Aircraft: {total_down}")

def readiness_percent(t, o):
    t = float(t)
    o = float(o)
    percentage = o / t * 100
    return percentage

main()
