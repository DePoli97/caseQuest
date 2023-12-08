import {createStore} from 'vuex';
import createPersistedState from "vuex-persistedstate";

export default createStore({
    plugins: [createPersistedState()],
    state() {
        return {
            camel_tests: [],
            kebab_tests: [],
            age: 0,
            gender: '',
            experience: 0,
            test_id: 0,
            device: '',
        }
    },
    getters: {
        getCamelTests(state) {
            return state.camel_tests
        },
        getKebabTests(state) {
            return state.kebab_tests
        },
        getAge(state) {
            return state.age
        },
        getGender(state) {
            return state.gender
        },
        getExperience(state) {
            return state.experience
        },
        getTestId(state) {
            return state.test_id
        },
        getDevice(state) {
            return state.device
        }
    },
    mutations: {
        setCamelTests(state, tests) {
            state.camel_tests = tests
        },
        setKebabTests(state, tests) {
            state.kebab_tests = tests
        },
        setAge(state, age) {
            state.age = age
        },
        setGender(state, gender) {
            state.gender = gender
        },
        setExperience(state, experience) {
            state.experience = experience
        },
        setTestId(state, test_id) {
            state.test_id = test_id
        },
        setDevice(state, device) {
            state.device = device
        }
    },
    actions: {
        async fetchTest(context) {
            let response = await fetch('http://localhost:8000/tests')
            let tests = await response.json()
            console.log(tests)
            context.commit('setCamelTests', tests[0])
            return context.commit('setKebabTests', tests[1])
        },
        setInfo(context, info) {
            context.commit('setAge', info.age)
            context.commit('setGender', info.gender)
            context.commit('setExperience', info.experience)
        },
        async saveResult(context, result) {
            let response = await fetch('http://localhost:8000/result', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(result)
            })
            let data = await response.json()
            console.log(data)
        },
        async getLastTestId(context) {
            let response = await fetch('http://localhost:8000/last_test_id')
            let data = await response.json()
            console.log(data)
            context.commit('setTestId', data)
        },
        async updateLastTestId(context) {
            let response = await fetch('http://localhost:8000/update_last_test_id')
            let data = await response.json()
            console.log(data)
        },
        setDevice(context, device) {
            console.log(device)
            let device_name = device.selectedDevice
            if (device_name === 'other')
                device_name = device.details
            context.commit('setDevice', device_name)
        }
    }
})
