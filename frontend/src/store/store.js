import {createStore} from 'vuex'
export default createStore({
    state() {
        return {
            camel_tests: [],
            kebab_tests: [],
            age: 0,
            gender: '',
            experience: 0
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
        }
    },
    actions: {
        async fetchTest(context) {
            let response = await fetch('http://localhost:8000/tests')
            let tests = await response.json()
            context.commit('setCamelTests', tests[0])
            return context.commit('setKebabTests', tests[1])
        },
        setInfo(context, info) {
            context.commit('setAge', info.age)
            context.commit('setGender', info.gender)
            context.commit('setExperience', info.experience)
        }
    }
})
