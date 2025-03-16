import React, { useState } from "react";
import { FlatList, ScrollView, StyleSheet, Text, View } from "react-native";
import { Button, Card, Provider, Searchbar } from "react-native-paper";
import Tapsiriqlar from "../../components/Home/Tapsiriqlar";
import { theme } from "../../theme";

function Home() {
  return (
    <ScrollView nestedScrollEnabled={true} theme={theme}>
      <View style={styles.header}>
        <Text
          style={{
            textAlign: "center",
            color: theme.colors.text,
            fontWeight: "bold",
            fontSize: 25,
          }}
        >
          Abbas Guliyev
        </Text>
        <View style={styles.detail}>
          <Text style={{ color: theme.colors.text, fontWeight: "bold", fontSize: 20 }}>
            10 Edilmiş
          </Text>
          <Text style={{ color: theme.colors.text, fontWeight: "bold", fontSize: 20 }}>
            |
          </Text>
          <Text style={{ color: theme.colors.text, fontWeight: "bold", fontSize: 20 }}>
            20 Gözləyən
          </Text>
        </View>
      </View>

      <Provider>
        <Tapsiriqlar />
      </Provider>
    </ScrollView>
  );
}

export default Home;

const styles = StyleSheet.create({
  header: {
    backgroundColor: theme.colors.primary,
    padding: 20,
    borderRadius: 20,
    margin: 15
  },
  detail: {
    flex: 1,
    flexDirection: "row",
    justifyContent: "space-between",
    margin: 30,
  },
});
