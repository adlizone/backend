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
    
        2.Get Itineraries for a Specific Tour
	    Endpoint: /api/tours/<int:tour_id>/itineraries/
            Method: GET

        3.Get Destinations for a Specific Tour
	    Endpoint: /api/tours/<int:tour_id>/destinations/
            Method: GET

        4.Get Categories for a Specific Tour
	    Endpoint: /api/tours/<int:tour_id>/categories/
            Method: GET 

        5.Get Filters for a Specific Tour
	    Endpoint: /api/tours/<int:tour_id>/filters/
            Method: GET