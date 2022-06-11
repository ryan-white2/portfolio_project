Title: My Pet ID (SQL Portfolio Project)

My Pet ID is a database that connects pets to owners along with vet information.
I have gone through several iterations on how I wanted this to work and I am still working out the small details as I progress in my knowledge of SQL. 

| Endpoint      | Methods       |Parameters     |
|---------------|---------------|---------------|
|/my_pet        |GET, POST, DELETE | <int:pet_id>|
|/pet_owner     |GET, POST, DELETE | <int:owner_id>|
|/vet_info      |GET, POST, DELETE | <int:vet_id>|

1. How did the project design evolve over time?
I simplified it a bit by taking out an extra table for a second owner. I've been on the road for the majority of theis course and it has been tough following along so i needed to simplify a bit. I think what i have done has been pretty good and i will continue to make it better and take more time to go through the material again and get a better understanding of all the concepts.

2. Did you choose to use an ORM or raw SQL? Why?
initially i thought about going through the raw SQL route but with time constraints i went with the twitter template and went about it throught the ORM way. As i worked through it i was getting a bit of a better understanding so im glad i went that route.

3. What future improvements are in store, if any? 
I think i will add a second owner table as well as break out the address column into multiple for city, state, zip instead of having it all on one line. Also adding an UPDATE method. I will continue to work on my project and make it better while submitting the variations on github to help track progress. 