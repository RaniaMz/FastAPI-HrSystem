print("Started Adding the Users.");
db = db.getSiblingDB("admin");
db.createUser({
  user: "rania",
  pwd: "pass123456",
  roles: [{ role: "readWrite", db: "admin" }],
});
print("End Adding the User Roles.");