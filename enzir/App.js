import { StatusBar } from "expo-status-bar";
import { SafeAreaView, ScrollView, StyleSheet, Text, TouchableOpacity, View } from "react-native";
import { createDrawerNavigator } from "@react-navigation/drawer";
import {
  NavigationContainer,
  useNavigation,
} from "@react-navigation/native";
import Home from "./pages/Home";
import { Ionicons } from "@expo/vector-icons";

const Drawer = createDrawerNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Drawer.Navigator
        screenOptions={({ navigation }) => ({
          headerLeft: () => (
            <TouchableOpacity
              onPress={() => navigation.openDrawer()}
              style={{ marginLeft: 10 }}
            >
              <Ionicons name="menu" size={24} color="black" />
            </TouchableOpacity>
          ),
        })}
      >
        <Drawer.Screen name="Home" component={Home} />
      </Drawer.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#677443",
    alignItems: "center",
    justifyContent: "center",
  },
});
