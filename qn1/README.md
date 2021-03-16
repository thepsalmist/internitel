# Intergration Protocols

#### By Xavier Frankline.

## Description

This describes the types of Intergration protocols

## Types of Intergration Protocols

The common types of Web Intergrations include REST (Representational state transfer) and GraphQL

### REST - Representational State Transfer

The REST design pattern centers on a uniform and predefined set of stateless operations that enables users to access and manipulate web data:

In REST architecture, APIs expose their functionality as resources which are then accessed by client. Every resource comes with a unique URI (Uniform Resource Identifier) that a client cant access by making requests to the server. WHen a client makes a request to the server it responds with the representation of the state of the queried resource.

Many REST implementations use the standard HTTP methods GET,POST,PUT,DELETE and PATCH. 

### GraphQL

The GraphQL is a query language that enables clients to make HTTP request and get responses.

GraphQL represents data as graphs with nodes and edges. Nodes represent objects while edges represent conections between nodes in the graph.

Unlike REST, GraphQL allows users to request data from several resources using a single request. The client can further specify the exact type of data to the server.


