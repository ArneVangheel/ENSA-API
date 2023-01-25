# Project Thema

Als project heb ik ervoor gekozen om een order api te maken. Dit is allemaal met een database verbonden, een table die de klanten accounts bewaard, een table voor de verschillende bestellingen, en dan een table die alle producten bewaard. Hierbij kan ik verschillende bestellingen voor bepaalde klanten aanmaken. Dit product kan ik kiezen uit de table, of ik kan ook nieuwe producten aanmaken. Ook heb ik het gemaakt, dat vooraleer je al deze dingen kunt doen moet inloggen/registreren op een website. Ook kan ik dan alle geregistreerde accounts bekijken, of data opvragen van een bepaalde klant. Ook kan ik een order aanpassen (dus bv de status naar Done zetten ipv Processing), en verwijderen.

> POST "/register" Hiermee kan je een account aanmaken die je later kunt gebruiken om de token op te vragen.<br>
> GET "/customers" Dit geeft een lijst van alle klanten accounts.<br>
> GET "/customer/{user_id}" Hiermee kan je van een bepaalde user (via de userid) gegevens opvragen, zoals email, bestellingen, naam, etc.<br>
> POST "/customers/{customer_id}/orders" Hiermee kan ik een order aanmaken op de naam van een bepaalde klant via id en het product kiezen.<br>
> GET "/orders" Dit laat alle orders zien die er gemaakt zijn.<br>
> PUT "/orders/{order_id}" Hiermee kan ik een bepaalde order aanpassen als je de orderid meegeeft.<br>
> DELETE "/orders/{order_id}" Hiermee kan je een order deleten aan de hand van een ordernummer.<br>
> GET "/products" Dit laat alle mogelijke producten zien.<br>
> POST "/products" Hiermee kan je een nieuw product aanmaken.<br>
> POST "/token" Hiermee kan je een token opvragen via bepaalde inloggegevens, deze token kan je gebruiken om bepaalde requests te doen.<br>
> GET "/users/me" Dit laat alle data zien van de gebruiken die is ingelogd via de token.<br>

## Links
* API Links
    * [API Repository](https://github.com/ArneVangheel/API-Eindproject)
    * [Hosted API](https://api-eindproject-arnevangheel.cloud.okteto.net/)
* Front-End Links
    * [Front-End Repository](https://github.com/ArneVangheel/website-eindproject)
    * [Hosted Front-End ](https://api-eindproject.netlify.app/)
   
## Uitbreidingen
(Alle algemene eisen zijn behaald)

   * 3.1 (+15%) Maak een front-end voor je applicatie die al je GET endpoints en POST endpoints bevat.
      * 3.1.1 (+10%) Host de front-end op Netlify. 
      * 3.1.2 (+10%) Geef de front-end een leuke stijlgeving.
     
## Eigen Aanvullingen 
   * PUT/DELETE requesten staan ook op de website
   * Meer endpoints dan nodig

## Postman (API Testing)
> POST "/register" Hiermee kan je een account aanmaken die je later kunt gebruiken om de token op te vragen.
![image](https://user-images.githubusercontent.com/94957070/209864116-5dbed187-1826-4a4c-abb8-5268b37708c3.png)
> POST "/token" Hiermee kan je een token opvragen via bepaalde inloggegevens, deze token kan je gebruiken om bepaalde requests te doen.
![image](https://user-images.githubusercontent.com/94957070/209864488-e8fde5f7-72d9-4954-ab02-3a3943f05baf.png)
GET "/customers" Dit geeft een lijst van alle klanten accounts.
![image](https://user-images.githubusercontent.com/94957070/209864704-7e72307f-401e-478f-8433-13f50230c946.png)
> GET "/customer/{user_id}" Hiermee kan je van een bepaalde user (via de userid) gegevens opvragen, zoals email, bestellingen, naam, etc.
![image](https://user-images.githubusercontent.com/94957070/209864755-6d46faf0-3889-41c1-ade9-0a4923319ebe.png)
> POST "/customers/{customer_id}/orders" Hiermee kan ik een order aanmaken op de naam van een bepaalde klant via id en het product kiezen.
![image](https://user-images.githubusercontent.com/94957070/209864936-a4ae5b03-f4ab-4d39-a9e1-a95f50644fd1.png)
> GET "/orders" Dit laat alle orders zien die er gemaakt zijn.
![image](https://user-images.githubusercontent.com/94957070/209864986-560f9389-1a0a-40f6-ab7f-aa43de000a5a.png)
> PUT "/orders/{order_id}" Hiermee kan ik een bepaalde order aanpassen als je de orderid meegeeft.
![image](https://user-images.githubusercontent.com/94957070/209865068-52b79a9f-4fae-4fe4-abbf-442c4b193554.png)
> DELETE "/orders/{order_id}" Hiermee kan je een order deleten aan de hand van een ordernummer.
![image](https://user-images.githubusercontent.com/94957070/209865140-184fe865-3ee8-497c-9168-fe039274a395.png)
> GET "/products" Dit laat alle mogelijke producten zien.
![image](https://user-images.githubusercontent.com/94957070/209865190-20e7b2f9-5112-4670-b2f9-81f1406f31f4.png)
> POST "/products" Hiermee kan je een nieuw product aanmaken.
![image](https://user-images.githubusercontent.com/94957070/209865271-243ccb73-c27d-4237-94a2-e0443a9d70d6.png)
> GET "/users/me" Dit laat alle data zien van de gebruiken die is ingelogd via de token.
![image](https://user-images.githubusercontent.com/94957070/209865330-c7d5f1ce-9d23-42ff-afbd-d78f923c7d63.png)


## OpenAPI Docs Screenshots
![image](https://user-images.githubusercontent.com/94957070/209861070-1af2c4b3-6e3e-49ff-acc6-c8a1f58c7ce8.png)
![screencapture-api-eindproject-arnevangheel-cloud-okteto-net-docs-2022-12-28-20_12_50](https://user-images.githubusercontent.com/94957070/209861294-3ac176b6-b41c-481c-a78b-f46d173fb0ea.png)


## Website
De website heeft zowel een login als registratie form, met een stijlgeving.
![image](https://user-images.githubusercontent.com/94957070/209861862-524d5539-aadf-4193-9c7e-02437e3104af.png)


