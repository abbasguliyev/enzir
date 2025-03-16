import React, { useState } from "react";
import { FlatList, StyleSheet, Text, View, ScrollView } from "react-native";
import { Button, Card, Searchbar } from "react-native-paper";
import { theme } from "../../theme";
import { useNavigation } from "@react-navigation/native";
const generateTasks = (count) => {
  return Array.from({ length: count }, (_, index) => ({
    id: index + 1,
    title: `Məşvərə ${index + 1}`,
    date: "03.07.2025",
  }));
};

const TASKS = generateTasks(50);

function Mesvere() {
  const navigation = useNavigation();

  const [searchQuery, setSearchQuery] = useState("");

  const [page, setPage] = useState(1);
  const itemsPerPage = 10;

  // Pagination üçün data
  const startIndex = (page - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const paginatedTasks = TASKS.slice(startIndex, endIndex);
  return (
    <ScrollView>
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
          nestedScrollEnabled={true}
          scrollEnabled={false}
          renderItem={({ item }) => (
            <Card style={styles.card}>
              <Card.Title title={item.title} />
              <Card.Content>
                <Text variant="bodyMedium">{item.date}</Text>
              </Card.Content>
              <Card.Actions>
                <Button
                  mode="contained"
                  buttonColor={theme.colors.secondary}
                  onPress={() => console.log("Edit", item.id)}
                >
                  Düzəlt
                </Button>
                <Button
                  mode="contained"
                  buttonColor={theme.colors.secondary}
                  onPress={() => navigation.navigate("MesvereQeydleri")}
                >
                  Ətraflı
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
    </ScrollView>
  );
}

export default Mesvere;

const styles = StyleSheet.create({
  searchBar: {
    marginTop: 20,
    marginHorizontal: 5,
  },
  container: {
    flex: 1,
    padding: 10,
    backgroundColor: theme.colors.background,
  },
  card: {
    marginVertical: 10,
    marginHorizontal: 10,
  },
  pagination: {
    flexDirection: "row",
    justifyContent: "space-between",
    marginTop: 10,
    alignItems: "center",
  },
});
