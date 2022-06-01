import React, { useEffect } from "react";
import AsyncStorage from "@react-native-community/async-storage";
import { Text, Button } from "react-native";
import Login from "./components/Login";
import Constants from "./libs/constants";

const App = () => {
  const onLogin = async (e) => {
    if (e.success)
      await AsyncStorage.setItem(Constants.LOCAL_KEY, JSON.stringify(e));
  };

  const logoutDone = async () => {
    await AsyncStorage.removeItem(Constants.LOCAL_KEY);
  };

  useEffect(() => {
    console.log({ userData: AsyncStorage.getItem(Constants.LOCAL_KEY) });
    // this shows {"_U": 0, "_V": 0, "_W": null, "_X": null}}
  }, []);

  const isLoggedIn = () => {
    let userJSON = AsyncStorage.getItem(Constants.LOCAL_KEY);

    return (
      userJSON != undefined && JSON.parse(userJSON).EmployeeId != undefined
    );
  };

  return !isLoggedIn() ? (
    <Login onLogin={onLogin} />
  ) : (
    <>
      <Text>{JSON.stringify(AsyncStorage.getItem(Constants.LOCAL_KEY))}</Text>
      <Button
        title="Logout"
        onPress={() => {
          logoutDone();
        }}
      ></Button>
    </>
  );
};

export default App;