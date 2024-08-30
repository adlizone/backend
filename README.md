THE TOURS MODULE

	The tour app is designed to manage and provide access to 
	tour packages and their associated itineraries. It serves as 
	a key component of the tour and travel booking website, allowing 
	users to browse available tours, view detailed itineraries, 
	and make bookings.



TOURS API USAGE

	1.Get All Tour Packages
            Endpoint: /api/tours/
            Method: GET

        2.Get a specific tour package
            Endpoint: /api/tours/id/
            Method: GET
    
        3.Get Itineraries for a Specific Tour
	    Endpoint: /api/tours/id/itineraries/
            Method: GET

        4.Get Destinations for a Specific Tour
	    Endpoint: /api/tours/id/destinations/
            Method: GET

        5.Get Categories for a Specific Tour
	    Endpoint: /api/tours/id/categories/
            Method: GET 

        6.Get Filters for a Specific Tour
	    Endpoint: /api/tours/id/filters/
            Method: GET
   
        7.Create a booking for a tour package
            Endpoint: /api/tours/bookings
            Method: POST

            Fields:
                customer_name
                customer_email
                customer_phone
                adults
                children
                arrival_date
                tour_package
                booking_date

        8.Search Tour package for a given category
             Endpoint: /api/tours/search/id
             Method: GET

        9.List of all available categories.
            Endpoint: /api/tours/categories
            Method: GET
