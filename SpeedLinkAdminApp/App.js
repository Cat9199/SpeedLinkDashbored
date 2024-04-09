import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, TouchableOpacity } from 'react-native';

const API_URL = 'http://192.168.1.118:8099'; // Replace 'your-api-url' with the actual API URL

const App = () => {
  const [shipments, setShipments] = useState([]);

  useEffect(() => {
    fetchShipments();
  }, []);

  const fetchShipments = async () => {
    try {
      const response = await fetch(`${API_URL}/api/app/shipments`);
      const data = await response.json();
      setShipments(data);
    } catch (error) {
      console.error('Error fetching shipments:', error);
    }
  };

  const renderItem = ({ item }) => (
    <TouchableOpacity onPress={() => viewShipmentDetails(item.id)}>
      <View style={{ padding: 10, borderBottomWidth: 1, borderBottomColor: '#ccc' }}>
        <Text>ID: {item.id}</Text>
        <Text>Barcode: {item.barcode}</Text>
        <Text>Status: {item.status}</Text>
      </View>
    </TouchableOpacity>
  );

  const viewShipmentDetails = async (id) => {
    try {
      const response = await fetch(`${API_URL}/api/shipments/${id}`);
      const data = await response.json();
      console.log('Shipment Details:', data);
      // Handle navigation or display details as needed
    } catch (error) {
      console.error('Error fetching shipment details:', error);
    }
  };

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text style={{ fontSize: 20, marginBottom: 10 }}>Shipments</Text>
      <FlatList
        data={shipments}
        renderItem={renderItem}
        keyExtractor={(item) => item.id.toString()}
        style={{ width: '100%' }}
      />
    </View>
  );
};

export default App;
