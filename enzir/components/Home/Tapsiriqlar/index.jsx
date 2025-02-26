import React, { useState } from "react";
import { FlatList, StyleSheet, Text, View } from "react-native";
import { Button, Card, Searchbar } from "react-native-paper";

const generateTasks = (count) => {
  return Array.from({ length: count }, (_, index) => ({
    id: index + 1,
    title: `Task ${index + 1}`,
    description: `This is the description for task ${index + 1}.`,
  }));
};

const TASKS = generateTasks(50);

export default function Tapsiriqlar() {
  const [searchQuery, setSearchQuery] = useState("");

  const [page, setPage] = useState(1);
  const itemsPerPage = 10;

  // Pagination üçün data
  const startIndex = (page - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const paginatedTasks = TASKS.slice(startIndex, endIndex);
  return (
    <View>
      <Searchbar
        placeholder="Axtar"
        onChangeText={setSearchQuery}
        value={searchQuery}
        style={styles.searchBar}
      />

      <View style={styles.container}>
        <FlatList
          data={paginatedTasks}
          keyExtractor={(item) => item.id.toString()}
          renderItem={({ item }) => (
            <Card style={styles.card}>
              <Card.Content>
                <Text variant="titleMedium">{item.title}</Text>
                <Text variant="bodyMedium">{item.description}</Text>
              </Card.Content>
              <Card.Actions>
                <Button
                  mode="contained"
                  buttonColor="#98653E"
                  onPress={() => console.log("Edit", item.id)}
                >
                  Edit
                </Button>
              </Card.Actions>
            </Card>
          )}
        />

        <View style={styles.pagination}>
          <Button disabled={page === 1} onPress={() => setPage(page - 1)}>
            Previous
          </Button>
          <Text>{page}</Text>
          <Button
            disabled={endIndex >= TASKS.length}
            onPress={() => setPage(page + 1)}
          >
            Next
          </Button>
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  searchBar: {
    marginTop: 20,
    marginHorizontal: 5,
  },
  container: {
    flex: 1,
    padding: 10,
    backgroundColor: "#f5f5f5",
  },
  card: {
    marginVertical: 10,
    marginHorizontal: 10
  },
  pagination: {
    flexDirection: "row",
    justifyContent: "space-between",
    marginTop: 10,
    alignItems: "center",
  }
});