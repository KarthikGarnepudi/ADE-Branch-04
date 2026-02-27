thisdisc={"brand":"ford","model":"mustang","Year":1994}
print(thisdisc["brand"]);

access dictionary items get(); keys();


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for child, info in myfamily.items():
    print(child)
    for key, value in info.items():
        print(key + ":", value)

        # sample changes