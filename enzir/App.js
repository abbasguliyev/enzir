import { StatusBar } from "expo-status-bar";
import { SafeAreaView, ScrollView, StyleSheet, Text, TouchableOpacity, View } from "react-native";
import { createStackNavigator } from "@react-navigation/stack";
import { createDrawerNavigator } from "@react-navigation/drawer";
import {
  NavigationContainer,
  useNavigation,
} from "@react-navigation/native";
import Home from "./pages/Home";
import { Ionicons } from "@expo/vector-icons";
import Mesvere from "./pages/Mesvere";
import Tapsiriqlar from "./components/Home/Tapsiriqlar";

import store from "./store";
import { Provider } from "react-redux";

const Stack = createStackNavigator();
const Drawer = createDrawerNavigator();

function DrawerNavigator() {
  return (
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
        <Drawer.Screen name="Ana Səhifə" component={Home} />
        <Drawer.Screen name="Məşvərə" component={Mesvere} />
      </Drawer.Navigator>
  );
}

export default function App() {
  return (
    <Provider store={store}>
      <NavigationContainer>
        <Stack.Navigator>
          {/* Drawer Navigasiyanı Stack içində saxlayırıq */}
          <Stack.Screen name="Drawer" component={DrawerNavigator} options={{ headerShown: false }} />
          
          {/* Bu səhifə yan menyuda OLMAYACAQ */}
          <Stack.Screen name="MesvereQeydleri" component={Tapsiriqlar} options={{ title: "Məşvərə Qeydləri" }} />
        </Stack.Navigator>
      </NavigationContainer>
    </Provider>
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
