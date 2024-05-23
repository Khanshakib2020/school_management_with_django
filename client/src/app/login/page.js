"use client"
import React, { useState } from 'react';
import Image from 'next/image';
import { AiFillUnlock } from 'react-icons/ai';
import { useRouter } from 'next/navigation';

const Login = () => {
  const router = useRouter();
  const [userDetails, setUserDetails] = useState({
    userName: '',
    password: '',
  });

  const handleChange = (e) => {
    setUserDetails((previousVal) => ({
      ...previousVal,
      [e.target.name]: e.target.value,
    }));
  };

  const handleLogin = (e) => {
    e.preventDefault();
    // Replace with your actual validation logic
    const mockUsername = 'testuser';
    const mockPassword = 'testpassword';

    if (
      userDetails.userName === mockUsername &&
      userDetails.password === mockPassword
    ) {
      console.log('Login successful', userDetails);
      router.push('/');
    } else {
      console.log('Invalid credentials');
    }
  };

  return (
    <>
      <div className="container d-flex justify-content-center align-items-center vh-100">
        <div className="card p-4">
          <div className="row">
            <div className="col-md-6">
              <div className="text-center mb-4">
                <img
                  src="/st.png"
                  alt="School Management App"
                  className="img-fluid img-size"
                />
              </div>
            </div>
            <div className="col-md-6">
              <div className="loginpage">
                <form className="p-10" onSubmit={handleLogin}>
                  <div className="text-center mb-4">
                    <span className="d-flex align-items-center justify-content-center">
                      <h3 className="mb-0 me-2">Login</h3>
                      <AiFillUnlock size={30} />
                    </span>
                  </div>

                  <div className="mb-3">
                    <label htmlFor="username" className="form-label">
                      Username
                    </label>
                    <input
                      type="text"
                      className="form-control"
                      id="username"
                      onChange={handleChange}
                      name="userName"
                    />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="password" className="form-label">
                      Password
                    </label>
                    <input
                      type="password"
                      className="form-control"
                      id="password"
                      onChange={handleChange}
                      name="password"
                    />
                  </div>
                  <div className="d-grid gap-2">
                    <button type="submit" className="btn btn-primary">
                      Login
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Login;
